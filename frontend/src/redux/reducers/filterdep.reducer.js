import {
    FETCH_DEPENDENCIES, FETCH_DEPENDENCIES_SUCCESS, FETCH_DEPENDENCIES_FAILURE
} from '../types';


const initialState = {
    filtersLoading: false,
    filtersFailure: false,
    errorMessage: '',
    dependArr: [],
    fetchdepSuccess: false,
    fetchError: false
};

const filtersDepReducer = (state = { ...initialState }, actions) => {
    switch (actions.type) {
        case FETCH_DEPENDENCIES:
            return { ...state, filtersLoading: true, fetchdepSuccess: false }
        case FETCH_DEPENDENCIES_SUCCESS:
            const dependArr = [...actions.payload.data]
            return {
                ...state,
                filtersLoading: true,
                dependArr: dependArr
            }
        case FETCH_DEPENDENCIES_FAILURE:
            return {
                ...state,
                fetchdepSuccess: false,
                filtersLoading: false,
                filtersFailure: true,
                fetchError: true,
                errorMessage: 'Failed to fetch dependencies',
            }
        default:
            return { ...state }
    }
};

export default filtersDepReducer;

