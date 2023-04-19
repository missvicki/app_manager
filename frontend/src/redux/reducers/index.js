import { combineReducers } from 'redux';
import authReducer from './auth.reducer';
import appsReducer from './apps.reducer';
import filtersFMReducer from './filterfm.reducer';
import filtersTMReducer from './filtertm.reducer';
import filtersDepReducer from './filterdep.reducer';

const reducerStates = {
    authState: authReducer, 
    appsState: appsReducer,
    filtersTMState: filtersTMReducer,
    filtersDepState: filtersDepReducer,
    filtersFMState: filtersFMReducer,
}
const rootReducer = combineReducers({ ...reducerStates })

export default rootReducer