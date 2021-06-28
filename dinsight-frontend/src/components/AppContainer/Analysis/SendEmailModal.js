import React, {useState} from 'react';
import { Modal } from 'react-bootstrap';
import { postQuery } from '../../util/firebase-realtime';
import createNotification from '../../util/Notification';
import {connect} from 'react-redux';

const SendEmailModal = (props) => {
    const {userID, handleClose, show, path} = props;
    const [email, setEmail] = useState('');
    const [subject, setSubject] = useState('');

    const handleSubmit = () => {
        if(email.length === 0 || subject.length == 0){
            createNotification('Email address and subject required !!', 'error');
            return;
        }

        postQuery(`emailRequests/${userID}`, {
            email,
            path,
            subject
        })
        .then(response => {
            setEmail('');
            setSubject('');
            createNotification('Email sent successfully !!', 'success');
            handleClose();
        })
        .catch(err => {
            console.error(err);
            createNotification('Some error occurred !', 'error');
        });
    }

    return (
        <Modal show={show} onHide={handleClose}>
            
            <Modal.Body>
                <div className="container">
                    <div className="row">
                        <div className="col p-2 text-center">
                            <div className="h3">Send report via email</div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col text-center">
                            
                                <div className="form-group p-3">
                                    <label htmlFor="email">Receiver's email address</label>
                                    <input 
                                        id="email" 
                                        type="email" 
                                        className="form-control" 
                                        required 
                                        onChange={(event) => setEmail(event.target.value)}
                                        value={email}
                                    />
                                </div>
                                <div className="form-group p-3">
                                    <label htmlFor="subject">Subject</label>
                                    <input 
                                        id="subject" 
                                        type="text" 
                                        className="form-control"
                                        required
                                        onChange={(event) => setSubject(event.target.value)}
                                        value={subject}
                                    />
                                </div>
                                {props.children}
                            
                        </div>
                    </div>
                </div>
            </Modal.Body>
            <Modal.Footer>
                <button className="btn btn-primary " type="button" onClick={handleSubmit}>Send</button>
                <button className="btn btn-danger float-end" type="button" onClick={handleClose}>cancel</button>
            </Modal.Footer>
        </Modal>
    )
}

const mapStateToProps = (state) => {
    if(!state.user)return {}
    return {
        userID : state.user.uid
    }
}
export default connect(mapStateToProps, {})(SendEmailModal);