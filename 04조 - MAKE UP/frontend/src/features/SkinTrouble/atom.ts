import { atom } from "recoil";

export const selectedSkinTroubleListState = atom<Array<string>>({
  key: 'selectedSkinTroubleListState',
  default: []
})