import { uploadPhoto, createUser } from './utils';
export default async function asyncUploadUser() {
  try {
    let img = await uploadPhoto();
    let usr = await createUser();
    return Promise.resolve({ img, usr });
  } catch (error) {
    return { photo: null, user: null };
  }
}
