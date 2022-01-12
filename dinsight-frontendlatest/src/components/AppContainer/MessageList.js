import React from 'react';
import { connect } from 'react-redux';

import MessageDetail from './MessageDetail';

class MessageList extends React.Component{
 
    componentDidMount = () => {
        setTimeout(()=>{
            this.scrollToBottom();
        },500)
    }

    componentDidUpdate = () => {
        setTimeout(()=>{
            this.scrollToBottom();
        },500)
    }

    renderMessages = () => {

        return this.props.messages.map((message) => {
            return <MessageDetail {...message} />
        });

    }


    scrollToBottom = () => {
        this.messagesEnd.scrollIntoView({ behavior: "smooth" ,block: "end", inline: "nearest",lignToTop: false});
    }


    render(){
        return (
            <div className="container-fluid" style={{overflowY:'scroll',overflowX:'hidden', position:'absolute', height:'90%'}}>
                <div className="ui list divided">
                    {this.renderMessages()}
                <div className="dummy-div" style={{height:'50px',clear:'both',float:'left'}}
                    ref={(el) => { this.messagesEnd = el; }} ></div>
                    
                </div>
            </div>
        );
    }
}

const mapStateToProps = (state) => {
    if(!state.user)return {};

    return {
        userID : state.user.uid,
        messages : state.messages
    };
}

export default connect(mapStateToProps, {postMessage})(MessageList);
