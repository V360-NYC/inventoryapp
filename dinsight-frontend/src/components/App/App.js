import React, {Component} from 'react';
import { library } from '@fortawesome/fontawesome-svg-core'
import { fab } from '@fortawesome/free-brands-svg-icons'
import {connect} from 'react-redux';
import { NotificationContainer } from 'react-notifications';

import AppContainer from '../AppContainer/AppContainer';
import SignIn from '../Authentication/SignIn';
import { changeAuthState, addInventoryFiles, addSummaryFiles, addMasterFiles } from '../../actions';
import {postQuery} from '../util/firebase-realtime';
import {getUserFiles} from '../util/firebase-firestore';
import createNotification  from '../util/Notification'; 
import { auth } from '../../config/firebase'
import LoadingSpinner from '../util/LoadingSpinner';

library.add(fab);

class App extends Component {

    state = {
        isLoading : true
    }

    fetchUserFiles = () => {
        getUserFiles(this.props.user.uid, 'inventoryFiles', this.props.addInventoryFiles);
        getUserFiles(
            this.props.user.uid, 
            'summaryFiles', 
            this.props.addSummaryFiles, 
            (files = []) => {
                files.forEach(file => {
                    createNotification('Summary File is available !!', 'success');
                    postQuery(`messages/${this.props.user.uid}`,{
                        botReply : true,
                        name : 'message from system',
                        photoUrl : '/images/logo.png',
                        fileAck : true,
                        text : `Latest summary file is now available.`,
                        downloadURL : file.downloadURL,
                        timestamp : Date.now()
                    })
                });

            });
        getUserFiles(this.props.user.uid, 'masterFiles', this.props.addMasterFiles);
    }
    
    componentDidMount = () => {
        auth.onAuthStateChanged(user => {
            this.props.changeAuthState(user)
            this.fetchUserFiles();
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
export default connect(mapStateToProps,{
    changeAuthState,
    addInventoryFiles,
    addMasterFiles,
    addSummaryFiles

})(App);