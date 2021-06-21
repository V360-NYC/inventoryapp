import React from 'react';
import { faFileExcel } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {connect } from 'react-redux';

import {uploadToStorage} from '../../util/firebase-storage';
import createNotification from '../../util/Notification';

class AddInventory extends React.Component{
    state = {
        inputKey : Date.now(),
        selectedFile : null,
        description : ''
    }

    onFileSelect = (event) => {
        this.setState({
            selectedFile : event.target.files[0]
        })
    }

    onDescriptionChanged = event =>{
        this.setState({
            description : event.target.value
        })
    }

    handleSubmit = event => {
        event.preventDefault();

        const filepath = `${this.props.userID}/${new Date().valueOf()}/${this.state.selectedFile.name}`;

        uploadToStorage(filepath, this.state.selectedFile)
        .then(response => {
            createNotification('File Uploaded successfully !!', 'success');
            this.setState({
                description:'',
                inputKey : Date.now()
            })
        })
        .catch(err => {
            createNotification('Some error occurred! Please try again', 'error');
        })

        
    }

    render(){
        return (
            <div className="container p-5">
                <div className="row justify-content-center">
                    <div className="col-12 col-sm-12 col-md-8 col-lg-6">
                        <div className="card border border-primary p-5 text-center" >
                            <div className="display-6">Upload Inventory File</div>
                            <form onSubmit={this.handleSubmit}>
                                <div className="form-group mx-2 mt-3 mb-2 pt-3 pb-3">
                                    <label htmlFor="file">Select your inventory file</label>
                                    <input 
                                        id="file" 
                                        key={this.state.inputKey}
                                        className="form-control" 
                                        type="file" 
                                        onChange={this.onFileSelect}
                                        required
                                    />
                                    <small id="fileHelp" class="form-text text-muted">Only .xlsx , .csv files are allowed</small>
                                </div>
                                <div className="form-group mx-2 mt-2 mb-3 pt-3 pb-3">
                                    <label htmlFor="description">Description</label>
                                    <textarea 
                                        id="description" 
                                        className="form-control"
                                        value={this.state.description}
                                        onChange={this.onDescriptionChanged}
                                    ></textarea>
                                </div>
                                <div className="form-group mx-2 mt-2 mb-3 pt-2 pb-3">
                                    <button className="btn btn-success">
                                        <FontAwesomeIcon icon={faFileExcel} size='2x'></FontAwesomeIcon> {'\u00A0'}{'\u00A0'}Upload
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        )
    }
}

const mapStateToProps = state => {
    if(!state.user)return {};

    return {
        userID : state.user.uid
    }
}

export default connect(mapStateToProps, {})(AddInventory);