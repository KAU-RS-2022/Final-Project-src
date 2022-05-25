import axios from 'axios';

const serverURL: string = "http://52.78.240.0/"; //개발 서버


export const apiClient = axios.create({
    baseURL: serverURL,
});


export const customApiClient = async (method: string, url: string) => {

    try {
        const result = await apiClient(url, {
            method: method,
        });

        return result.data;
    }
    catch (err: any) {
        console.log(err.response);
        console.log(err.message);

        if (!err.response) {
            return 'Network Error';
        }

        return null
    }
}