import React from 'react';
import { faFileExcel, faThList } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {connect } from 'react-redux';
import {v4 as uuidv4} from 'uuid';

import { addFileMetaData, postQuery, getUserVendors} from '../../util/firebase-firestore';
import {uploadToStorage} from '../../util/firebase-storage';
import createNotification from '../../util/Notification';
import FileInput from './FileInput';
import AddVendorModalContainer from './AddVendorModalContainer';
import { date } from 'yup';
import Moment from 'moment';


class AddInventory extends React.Component{
    state = {
        fileInputs : [{
            id : Date.now(),
            selectedFile:null
        }],
        description:'',
        inputDisabled : false,
        vendors : [],
        date : Moment().format('YYYY-MM-DD'),
        VENDORNAME : ''

    }

    
    componentDidMount = () => {
        // fetch all user vendors
        getUserVendors(this.props.userID)
        .then(vendors => this.setState({vendors}))
        .catch(err => console.error(err));
    }

    addFileInput = () => {
        const N = this.state.fileInputs.length;
        if(this.state.fileInputs[N - 1].selectedFile === null){
            createNotification('Please select file first !', 'warning');
            return;
        }

        if(N === 5){
            createNotification('Limit reached !', 'warning');
            return;
        }

        this.setState({
            fileInputs : [...this.state.fileInputs, {selectedFile:null, id: Date.now()}]
        })
    }

    onFileSelect = (id, selectedFile) => {
        // const index = this.state.fileInputs.findIndex(input => input.id === id)[0];
        const rest = this.state.fileInputs.filter(input => input.id != id)
        // this.setState({
        //     fileInputs : [...this.state.fileInputs.splice(0, index), {
        //         id : this.state.fileInputs[index].id,
        //         selectedFile : selectedFile
        //     }, ]
        // })

        this.setState({
            fileInputs : [...rest, {id, selectedFile}]
        })
    }

    onDescriptionChanged = event =>{
        this.setState({
            description : event.target.value
        })
    }

    removeFileInput = (id) => {

        if(this.state.fileInputs.length === 1){
            createNotification('Must upload atleast One file', 'warning');
            return;
        }

        this.setState({
            fileInputs : this.state.fileInputs.filter(input => input.id !== id)
        })
    }

    handleSubmit = event => {
        event.preventDefault();
        
        this.setState({
            inputDisabled : true
        })

        const datetimeConstructor = new Intl.DateTimeFormat("en",{
            hour:'2-digit',
            minute:'2-digit',
            second:'2-digit',
            hour12:false
        });


        const datetime = new Date()
        const timeString = datetimeConstructor.format(datetime);

        const datetimeString = `${this.state.date}T${timeString}`;
        // console.log(datetimeString);
        const TIMESTAMP = new Date(datetimeString).getTime();
        console.log(typeof(TIMESTAMP));

        const BUCKET = 'fileuploadsbusinessassist';
        
        const BASE_DIR = `${BUCKET}/${this.props.userID}/${TIMESTAMP}`
        const files = this.state.fileInputs.map(input => {
            const filepath = `${BASE_DIR}/${input.selectedFile.name}`;

            // return new Promise((resolve, reject) => {
            //     setTimeout(resolve(), 5000);
            // })
            return uploadToStorage(filepath, input.selectedFile)
            // .then(response => {
            //     createNotification(`${input.selectedFile.name} File Uploaded`, 'success');
                
            // })
            // .catch(err => {
            //     createNotification('Some error occurred! Please try again', 'error');
            // })
        })

        Promise.all(files)
        .then(response => {
            createNotification(`Files Uploaded`, 'success');
            const data = {
                bucket : BUCKET,
                CREATEDAT : TIMESTAMP,
                VENDORNAME : this.state.VENDORNAME,
                description : this.state.description
            }
            
            data.files = this.state.fileInputs.map(input => {
                return {
                    filePath : `${this.props.userID}/${data.CREATEDAT}/${input.selectedFile.name}`
                }
            })
            // console.log(data)
            postQuery(`fileUploads`, data);
            
            this.setState({
                fileInputs : [{
                    id : Date.now(),
                    selectedFile : null
                }],
                inputDisabled : false,
                description:'',
                VENDORNAME:'',
                date : Moment().format('YYYY-MM-DD')
            })
        })
        .catch(err =>{
            createNotification(`Upload failed`, 'error');
            console.error(err);
            this.setState({
                fileInputs : [{
                    id : Date.now(),
                    selectedFile : null,
                }],
                inputDisabled : false,
                description:'',
                VENDORNAME:'',
                date : Moment().format('YYYY-MM-DD')
            })
        })
        
        
    }

    renderFileInputs = () => {
        return this.state.fileInputs.map(({id, selectedFile}, index) => {
            return (
                <div className="form-group mx-2 mt-3 mb-2 pt-3 pb-3">
                    <label htmlFor={id}>Select your inventory file</label>
                    <FileInput 
                        id={id} 
                        onFileSelect={this.onFileSelect}
                        removeFileInput={this.removeFileInput}
                    />
                    <small id="fileHelp" class="form-text text-muted">Only .xlsx , .csv , .xls files are allowed</small>
                </div>
            )
        })
    }

    renderUserVendors = () => {
        
        const vendorList = this.state.vendors.map((vendor, index) => {
            return (
                <option value={vendor.VENDORNAME} key={index}>{vendor.VENDORNAME}</option>
            )
        });
        
        
        return [
            <option disabled selected value=""> --- Select a Vendor --- </option>,
            ...vendorList,
            (vendorList.length === 0)?<option disabled>No vendors available</option>:null
        ];
    }

    addNewVendor = (vendor) => {
        
        postQuery('userVendors', {
            ...vendor,
            userID : this.props.userID
        })
        this.setState({
            vendors : [...this.state.vendors, {...vendor}]
        })
    }
    
    render(){
        
        return (
            <div className="container p-5">
                <form onSubmit={this.handleSubmit}>
                    <div className="row justify-content-center">
                        <div className="col-12 col-sm-12 col-md-12 col-lg-6 text-center">
                            <div className="h3">Upload Inventory File</div>
                        </div>
                    </div>
                    <div className="row justify-content-center ">
                        <div className="col-12 col-sm-12 col-md-12 col-lg-6 text-center">
                            
                                    <div className="form-group py-2 mt-3 mb-2">
                                        <label htmlFor="date">Enter Date</label>
                                        <input 
                                            type="date" 
                                            className="form-control"
                                            id="date" 
                                            value={this.state.date}
                                            onChange={(e) => this.setState({date : e.target.value})}
                                            required
                                        />
                                    </div>
                                
                                    <div className="form-group py-2 mt-3 mb-2">
                                        <label htmlFor="VENDORNAME">Select Vendor</label>
                                        <select 
                                            className='form-select'
                                            value={this.state.VENDORNAME}
                                            onChange={(e) => this.setState({VENDORNAME : e.target.value})}
                                            id="VENDORNAME"
                                            required
                                        >
                                            {this.renderUserVendors()}
                                        </select>
                                        
                                    </div>
                            
                            <AddVendorModalContainer addNewVendor={this.addNewVendor}/>
                        </div>
                    </div>
                    <div className="row justify-content-center">
                        <div className="col-12 col-sm-12 col-md-12 col-lg-6 text-center">
                            
                            
                                {this.renderFileInputs()}
                                <div className="form-group mx-2 mt-3 mb-2 pt-3 pb-3">
                                    <button className="btn btn-outline" onClick={this.addFileInput} disabled={this.state.disabled} type="button">Select More Files</button>
                                </div>
                                <div className="form-group mx-2 mt-2 mb-3 pt-3 pb-3">
                                    <label htmlFor="description">Description</label>
                                    <textarea 
                                        id="description" 
                                        className="form-control"
                                        value={this.state.description}
                                        onChange={e => this.setState({description:e.target.value})}
                                    ></textarea>
                                </div>
                                <div className="form-group mx-2 mt-2 mb-3 pt-2 pb-3">
                                    <button className="btn btn-success" disabled={this.state.inputDisabled}>
                                        <FontAwesomeIcon icon={faFileExcel} size='2x'></FontAwesomeIcon> {'\u00A0'}{'\u00A0'}Upload
                                    </button>
                                </div>
                            
                        </div>

                    </div>
                </form>
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