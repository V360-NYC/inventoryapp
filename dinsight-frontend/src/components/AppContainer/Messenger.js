import React from 'react';
import { List, Image } from 'semantic-ui-react';
import { MDBCard, MDBInput } from 'mdbreact';
import {connect } from 'react-redux';

import '../../assets/css/Messenger.css';
import MessageList from './MessageList';
import {postMessage} from '../../actions';
import { postQuery } from '../util/firebase-realtime';

class Messenger extends React.Component{
    state = {
        queryText : ''
    }

    handleQuerySubmit = (event) => {
        event.preventDefault();
        

        if(this.state.queryText.length == 0)return;
        const {displayName, uid, photoURL} = this.props.user;

        postQuery(`messages/${uid}`,{
            name: displayName,
			text: this.state.queryText,
			photoUrl: photoURL,
			uid: uid,
			timeStamp: new Date().valueOf(),
			device: "desktop"
        })
        .then(response => {
        
        })
        .catch(err => console.error(err));

        this.setState({
            queryText:''
        })
    }

    onInputChange = (event) => {
        this.setState({
            queryText : event.target.value
        })
    }

    render = () => {
        return (
            <div className="container mt-4 ">
                <div className="row d-flex justify-content-center">
                    <div className="col-12 col-md-10 col-lg-8" style={{position:'relative'}}>
                        <MDBCard style={{height:'85vh'}} >
                            <MessageList />
                            <div className="container align-bottom" style={{position:'absolute', bottom:'0', height:'80px'}}>
                                <form onSubmit={this.handleQuerySubmit}>
                                    <div className="row flex-nowrap">
                                        <div className="col-9">
                                            <MDBInput
                                                label="Type your query here"
                                                type="text"
                                                value={this.state.queryText}
                                                onChange={this.onInputChange}
                                            />
                                        </div>
                                        <div className="col d-flex justify-content-center align-items-center">
                                            <button className="btn btn-default btn-md" >Send</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </MDBCard>
                    </div>
                </div>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    if(!state.user)return {};

    return {
        user : state.user
    }
}

export default connect(mapStateToProps,{postMessage})(Messenger);
