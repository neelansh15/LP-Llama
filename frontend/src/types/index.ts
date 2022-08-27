export interface Item {
  name?: string;
  token0?: string;
  token1?: string;
  apy: number;
  chain: number;
  exchange: string;
}

export interface Header {
  label: string;
  key: string;
}
