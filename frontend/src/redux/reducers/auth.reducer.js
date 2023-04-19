const intitialSate = {

}

const authReducer = (state = intitialSate, actions) => {
    switch (actions.type) {
        case 'AUTH_REDUCER_RESET':
            return { ...intitialSate };
        default:
            return { ...state };
    }
}

export default authReducer