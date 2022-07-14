import React from 'react';
import Messenger from './Messenger';
import Navigation from './Navigation/Navigation';
import AddInventory from './Inventory/AddInventory';

import { BrowserRouter, Route } from 'react-router-dom'
import Analysis from './Analysis/Analysis';
import Divider from '../AppContainer/divider'
const AppContainer = () => {
    return (
        <>
        
        <BrowserRouter>
            <Divider/>
            <Navigation />
            {/* <Route exact path='/' component={Messenger} /> */}
            <Route exact path='/' component={AddInventory } />
            {/* Initially the / path was for Messenger now it is for inventory and the /analysis is for analysis */}
            {/* <Route exact path='/inventory' component={AddInventory} /> */}
            <Route exact path='/analysis' component={Analysis} />
        </BrowserRouter>
        </>
    )
}

export default AppContainer;