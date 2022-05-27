import React from 'react';
import Messenger from './Messenger';
import Navigation from './Navigation/Navigation';
import AddInventory from './Inventory/AddInventory';

import { BrowserRouter, Route } from 'react-router-dom'
import Analysis from './Analysis/Analysis';
const AppContainer = () => {
    return (
        <>
        
        <BrowserRouter>
            <Navigation />
            {/* <Route exact path='/' component={Messenger } /> */}
            <Route exact path='/' component={AddInventory} />
            <Route exact path='/analysis' component={Analysis} />
        </BrowserRouter>
        </>
    )
}

export default AppContainer;