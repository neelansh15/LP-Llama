export const BASE_URL = "https://sharp-geese-cry-115-110-248-75.loca.lt/";

export const chainTokens = {
  1: "eth",
  137: "matic",
  56: "bnb",
} as Record<number, string>;

export const chainNames = {
  1: "Ethereum",
  137: "Polygon",
  56: "Binance Smart Chain",
} as Record<number, string>;

export const explorerUrls = {
  1: "https://etherscan.io",
  4: "https://rinkeby.etherscan.io",
  56: "https://bscscan.com/",
  97: "https://testnet.bscscan.com",
  137: "https://polygonscan.com",
  250: "https://ftmscan.com",
  4002: "https://testnet.ftmscan.com",
  43113: "https://cchain.explorer.avax-test.network",
  43114: "https://snowtrace.io",
  80001: "https://mumbai.polygonscan.com",
  1666700000: "https://explorer.pops.one",
} as Record<number, string>;

export const exchangeLogos = {
  sushiswap: "https://sushi.com/_next/static/media/logo.d019d88b.png",
  pancakeswap:
    "https://pancakeswap.finance/images/tokens/0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82.png",
} as Record<string, string>;
