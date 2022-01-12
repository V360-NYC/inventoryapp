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

export const addUserVendor = (vendor) => {
    return {
        type : 'ADD_VENDOR',
        payload : vendor
    }
}

export const addInventoryFiles = (files) => {
    return {
        type : 'ADD_INVENTORY_FILES',
        payload : files
    }
}

export const addMasterFiles = (files) => {
    return {
        type : 'ADD_MASTER_FILES',
        payload : files
    }
}

export const addSummaryFiles = (files) => {
    return {
        type : 'ADD_SUMMARY_FILES',
        payload : files
    }
}