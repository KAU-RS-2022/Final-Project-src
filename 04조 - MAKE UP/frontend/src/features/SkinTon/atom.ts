import { atom } from "recoil";

export const selectedSkinTonState = atom<string>({
  key:'selectedSkinTonState',
  default:''
});