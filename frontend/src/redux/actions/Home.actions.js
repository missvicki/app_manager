import { FETCH_APPS, FETCH_APPS_FAILURE, FETCH_APPS_SUCCESS } from '../types';
import { createAction } from './helpers.actions';
import ApiHandler from '../../api/AxiosApi';


const appsActions = (dispatch) => {
    const fetchApps = async () => {
        dispatch(createAction(FETCH_APPS))
        try {
            const response = await ApiHandler.apiRequest('GET', 'apps', 'create-get', undefined, false)
            if (![200, 201].includes(response.status)) {
                return dispatch(createAction(FETCH_APPS_FAILURE, { error: response.data }))
            }

            return dispatch(createAction(FETCH_APPS_SUCCESS, { data: response.data }))
        } catch (error) {
            dispatch(createAction(FETCH_APPS_FAILURE, { error: error.message }))
        }
    };

    return {
        fetchApps
    }
};

export default appsActions;