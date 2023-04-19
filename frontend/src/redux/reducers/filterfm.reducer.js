import {
    FETCH_FUNCTIONAL_MAINTAINER, FETCH_FUNCTIONAL_MAINTAINER_SUCCESS, FETCH_FUNCTIONAL_MAINTAINER_FAILURE
} from '../types';


const initialState = {
    filtersLoading: false,
    filtersFailure: false,
    errorMessage: '',
    funcMaintainArr: [],
    fetchfmSuccess: false,
    fetchError: false
};

const filtersFMReducer = (state = { ...initialState }, actions) => {
    switch (actions.type) {
        
        case FETCH_FUNCTIONAL_MAINTAINER:
            return { ...state, filtersLoading: true, fetchfmSuccess: false }
        case FETCH_FUNCTIONAL_MAINTAINER_SUCCESS:
            const funcMaintainArr = [...actions.payload.data]
            return {
                ...state,
                filtersLoading: true,
                funcMaintainArr: funcMaintainArr
            }
        case FETCH_FUNCTIONAL_MAINTAINER_FAILURE:
            return {
                ...state,
                fetchfmSuccess: false,
                filtersLoading: false,
                filtersFailure: true,
                fetchError: true,
                errorMessage: 'Failed to fetch functional maintainers',
            }
        default:
            return { ...state }
    }
};

export default filtersFMReducer;

