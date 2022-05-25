import { atom } from "recoil";

export const selectedDangerElementListState = atom<Array<string>>({
  key: 'selectedDangerElementListState',
  default: []
})