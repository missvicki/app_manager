import {
    POST_APP, POST_APP_SUCCESS, POST_APP_FAILURE,
    FETCH_APPS, FETCH_APPS_SUCCESS, FETCH_APPS_FAILURE,
    UPDATE_APP, UPDATE_APP_FAILURE, UPDATE_APP_SUCCESS
} from '../types';


const initialState = {
    appsLoading: false,
    appsFailure: false,
    errorMessage: '',
    updateappsuccess: false,
    apps: [],
    fetchappsSuccess: false,
    fetchError: false
};

const appsReducer = (state = { ...initialState }, actions) => {
    switch (actions.type) {
        case FETCH_APPS:
            return { ...state, appsLoading: true, fetchappsSuccess: false }
        case FETCH_APPS_SUCCESS:
            const apps = [...actions.payload.data]
            return {
                ...state,
                appsLoading: true,
                apps: apps
            }
        case FETCH_APPS_FAILURE:
            return {
                ...state,
                fetchappsSuccess: false,
                appsLoading: false,
                appsFailure: true,
                fetchError: true,
                errorMessage: 'Failed to fetch apps',
            }
        default:
            return { ...state }
    }
};

export default appsReducer;

