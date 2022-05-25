import { atom } from 'recoil';

export const selectedSkinTypeState  = atom<string>({
  key: 'selectedSkinTypeState',
  default:''
});