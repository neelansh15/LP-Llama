export function getIconUrl(name: string | undefined): string {
  if (!name) return "";

  if (name === "WETH") name = "ETH";
  const BASE_URL =
    "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/svg/icon/";
  const result = `${BASE_URL}${name.toLowerCase()}.svg`;

  return result;
}

export function onImageError(event: any) {
  event.target.src = "/ban.svg";
}
