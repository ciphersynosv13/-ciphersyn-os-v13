-- WALLETS
create table if not exists wallets (
  user_id uuid primary key references auth.users(id) on delete cascade,
  coins int default 0 not null,
  updated_at timestamptz default now()
);

-- TRANSACTIONS
create table if not exists coin_transactions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id),
  coins int not null,
  amount int not null,
  currency text not null,
  provider text,
  status text default 'success',
  created_at timestamptz default now()
);

-- BOOSTS
create table if not exists boosts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id),
  post_id uuid,
  type text check (type in ('views','likes','followers','chat')),
  coins_spent int,
  expires_at timestamptz,
  created_at timestamptz default now()
);

-- AUTO CREATE WALLET
create or replace function handle_new_wallet() returns trigger as $$
begin insert into public.wallets (user_id, coins) values (new.id, 50); return new; end; $$ language plpgsql;
drop trigger if exists on_auth_user_created_wallet on auth.users;
create trigger on_auth_user_created_wallet after insert on auth.users for each row execute function handle_new_wallet();

-- RLS
alter table wallets enable row level security;
alter table boosts enable row level security;
create policy "own wallet" on wallets for all using (auth.uid() = user_id);
create policy "own boosts" on boosts for all using (auth.uid() = user_id);
create policy "read active boosts" on boosts for select using (expires_at > now());
