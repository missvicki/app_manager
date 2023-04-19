import {
    FETCH_TECHNICAL_MAINTAINER, FETCH_TECHNICAL_MAINTAINER_FAILURE, FETCH_TECHNICAL_MAINTAINER_SUCCESS,
    FETCH_FUNCTIONAL_MAINTAINER, FETCH_FUNCTIONAL_MAINTAINER_FAILURE, FETCH_FUNCTIONAL_MAINTAINER_SUCCESS,
    FETCH_DEPENDENCIES, FETCH_DEPENDENCIES_FAILURE, FETCH_DEPENDENCIES_SUCCESS
} from '../types';
import { createAction } from './helpers.actions';
import ApiHandler from '../../api/AxiosApi';


export const fetch_technical_maintainers = (dispatch) => {
    const fetchTM = async () => {
        dispatch(createAction(FETCH_TECHNICAL_MAINTAINER))
        try {
            const response = await ApiHandler.apiRequest('GET', 'technical_maintainers', ' ', undefined, false)
            if (![200, 201].includes(response.status)) {
                return dispatch(createAction(FETCH_TECHNICAL_MAINTAINER_FAILURE, { error: response.data }))
            }

            return dispatch(createAction(FETCH_TECHNICAL_MAINTAINER_SUCCESS, { data: response.data }))
        } catch (error) {
            dispatch(createAction(FETCH_TECHNICAL_MAINTAINER_FAILURE, { error: error.message }))
        }
    };

    return {
        fetchTM
    }
};

export const fetch_functional_maintainers = (dispatch) => {
    const fetchFM = async () => {
        dispatch(createAction(FETCH_FUNCTIONAL_MAINTAINER))
        try {
            const response = await ApiHandler.apiRequest('GET', 'functional_maintainers', ' ', undefined, false)
            if (![200, 201].includes(response.status)) {
                return dispatch(createAction(FETCH_FUNCTIONAL_MAINTAINER_FAILURE, { error: response.data }))
            }

            return dispatch(createAction(FETCH_FUNCTIONAL_MAINTAINER_SUCCESS, { data: response.data }))
        } catch (error) {
            dispatch(createAction(FETCH_FUNCTIONAL_MAINTAINER_FAILURE, { error: error.message }))
        }
    };

    return {
        fetchFM
    }
};

export const fetch_dependencies = (dispatch) => {
    const fetchDep = async () => {
        dispatch(createAction(FETCH_DEPENDENCIES))
        try {
            const response = await ApiHandler.apiRequest('GET', 'dependencies', ' ', undefined, false)
            if (![200, 201].includes(response.status)) {
                return dispatch(createAction(FETCH_DEPENDENCIES_FAILURE, { error: response.data }))
            }

            return dispatch(createAction(FETCH_DEPENDENCIES_SUCCESS, { data: response.data }))
        } catch (error) {
            dispatch(createAction(FETCH_DEPENDENCIES_FAILURE, { error: error.message }))
        }
    };

    return {
        fetchDep
    }
};
