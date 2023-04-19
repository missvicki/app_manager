import {
    FETCH_TECHNICAL_MAINTAINER, FETCH_TECHNICAL_MAINTAINER_SUCCESS, FETCH_TECHNICAL_MAINTAINER_FAILURE
} from '../types';


const initialState = {
    filtersLoading: false,
    filtersFailure: false,
    errorMessage: '',
    techMaintainArr: [],
    fetchtmSuccess: false,
    fetchError: false
};

const filtersTMReducer = (state = { ...initialState }, actions) => {
    switch (actions.type) {
        case FETCH_TECHNICAL_MAINTAINER:
            return { ...state, filtersLoading: true, fetchtmSuccess: false }
        case FETCH_TECHNICAL_MAINTAINER_SUCCESS:
            const techMaintainArr = [...actions.payload.data]
            return {
                ...state,
                filtersLoading: true,
                techMaintainArr: techMaintainArr
            }
        case FETCH_TECHNICAL_MAINTAINER_FAILURE:
            return {
                ...state,
                fetchtmSuccess: false,
                filtersLoading: false,
                filtersFailure: true,
                fetchError: true,
                errorMessage: 'Failed to fetch technical maintainers',
            }
        default:
            return { ...state }
    }
};

export default filtersTMReducer;

