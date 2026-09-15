export const PACKS = [
  { id: 'starter', coins: 100, bonus: 0, prices: { NGN: 500, USD: 1.99, EUR: 1.99, GBP: 1.79, KES: 300, GHS: 30, ZAR: 40, INR: 169 } },
  { id: 'popular', coins: 250, bonus: 50, prices: { NGN: 1000, USD: 3.99, EUR: 3.99, GBP: 3.49, KES: 600, GHS: 60, ZAR: 80, INR: 349 } },
  { id: 'best', coins: 600, bonus: 200, prices: { NGN: 2000, USD: 7.99, EUR: 7.99, GBP: 6.99, KES: 1200, GHS: 120, ZAR: 160, INR: 699 } },
  { id: 'baller', coins: 1500, bonus: 600, prices: { NGN: 5000, USD: 19.99, EUR: 19.99, GBP: 17.99, KES: 3000, GHS: 300, ZAR: 400, INR: 1699 } },
];

export const BOOST_COST = { views: 100, likes: 100, followers: 250, chat: 150 };
export function getUserCurrency() {
  try {
    const c = Intl.NumberFormat().resolvedOptions().locale;
    if(c.includes('NG')) return 'NGN';
    if(c.includes('GH')) return 'GHS';
    if(c.includes('KE')) return 'KES';
    if(c.includes('ZA')) return 'ZAR';
    if(c.includes('IN')) return 'INR';
    if(c.includes('GB')) return 'GBP';
    if(c.includes('EU')||c.includes('DE')||c.includes('FR')) return 'EUR';
    return 'USD';
  } catch { return 'NGN'; }
}
