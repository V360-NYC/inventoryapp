import { combineReducers } from 'redux';

const AuthStateReducer = (currentState = null, action) => {    
    if(action.type === 'CHANGE_AUTH_STATE'){
        return action.payload;
    }
    return currentState;
}

const messagesReducer = (messages = [], action) => {
    if(action.type === 'POST_MESSAGE'){
        const index = messages.findIndex(message => message.key === action.payload.key)
        if(index === -1)return [...messages, action.payload];
        
        return [
            ...messages.slice(0, index),
            action.payload, ...messages.slice(index + 1)
        ]
    }
    return messages;
}

const vendorsReducer = (vendors = [], action) => {
    if(action.type === 'ADD_VENDOR'){
        return [...vendors, action.payload];
    }
    return vendors
}

export default combineReducers({
    user:AuthStateReducer,
    messages: messagesReducer,
    vendors : vendorsReducer
});