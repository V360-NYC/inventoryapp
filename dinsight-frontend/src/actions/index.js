export const changeAuthState = (user) => {
    
    return {
        type:'CHANGE_AUTH_STATE',
        payload : user
    }
}

export const postMessage = (message) => {
    return {
        type : 'POST_MESSAGE',
        payload: message
    }
}