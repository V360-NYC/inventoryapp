import React, {Component} from 'react';
import { library } from '@fortawesome/fontawesome-svg-core'
import { fab } from '@fortawesome/free-brands-svg-icons'
import {connect} from 'react-redux';
import { NotificationContainer } from 'react-notifications';

import AppContainer from '../AppContainer/AppContainer';
import SignIn from '../Authentication/SignIn';
import { changeAuthState } from '../../actions';
import { auth } from '../../config/firebase'
import LoadingSpinner from '../util/LoadingSpinner';

library.add(fab);

class App extends Component {

    state = {
        isLoading : true
    }
    
    componentDidMount = () => {
        auth.onAuthStateChanged(user => {
            this.props.changeAuthState(user)

            this.setState({
                isLoading:false
            })
        });
    }

    renderApp = () => {
        if(this.state.isLoading){
            return (
                <div className="container d-flex justify-content-center" style={{paddingTop:'15%'}}>
                    <LoadingSpinner  />
                </div>
            )
        }
        if(this.props.user){
            return <AppContainer />
        }
        return <SignIn />
    }

    render = ()=>{
        return (
            <div>
                <NotificationContainer />
                {this.renderApp()}
            </div>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        user : state.user
    };
}
export default connect(mapStateToProps,{changeAuthState})(App);