import React from 'react';
import { faFileExcel } from '@fortawesome/free-regular-svg-icons'
import { faCloudDownloadAlt, faEnvelopeOpen } from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { MDBTable, 
        MDBTableHead, 
        MDBTableBody, 
        MDBTooltip,
        MDBCard, 
        MDBCardBody, 
        MDBCardHeader,
        MDBDataTableV5 } from 'mdbreact'


import LoadingSpinner from '../../util/LoadingSpinner';
import SendEmailModal from '../Analysis/SendEmailModal';

class VendorFileList extends React.Component{

    state = {
        show : false,
        selectedFile : null
    }

    showModal = (type, createdAt, filePath) => {

        this.setState({
            show:true,
            selectedFile : {
                type,
                createdAt,
                filePath
            }
        })
    }
    handleClose = () => {
        this.setState({
            show : false
        })
    }
   
    renderTableBody = (data) => {
        const datetimeConstructor = new Intl.DateTimeFormat("en",{
            day : '2-digit',
            weekday : 'short',
            month:'long',
            year : 'numeric'
        });

        const columns = [
            {
                label : 'last modified',
                field : 'file',
                width : 50
            },
            {
                label : 'Action',
                field : 'action',
                width : 50
            }
        ]

        const rows = data.map(({createdAt, downloadURL, type, filePath}) => {
            const date = new Date(createdAt.toDate());
            return {
                file : (
                    <>
                        <FontAwesomeIcon icon={faFileExcel} size='2x' style={{color:'gray'}}/> {'\u00A0'}{'\u00A0'} {datetimeConstructor.format(date)}
                    </>
                ),
                action : (
                    <>
                        <div className="d-flex">
                            <div className="d-inline-block px-2">
                                <MDBTooltip domElement tag="span" placement="top">
                                    <a onClick={() => this.showModal(type,datetimeConstructor.format(date), filePath)}><span className="text-primary"> <FontAwesomeIcon icon={faEnvelopeOpen} size='2x'/></span></a>
                                    <span>Send via email</span>         
                                </MDBTooltip>
                            </div>
                            <div className="d-inline-block px-2">
                                <MDBTooltip domElement tag="span" placement="top">
                                    <a href={downloadURL} target="_blank"><span className="text-primary"> <FontAwesomeIcon icon={faCloudDownloadAlt} size='2x'/></span></a>
                                    <span>Download File to this device.</span>

                                </MDBTooltip>
                            </div>
                        </div>
                    </>
                )
            }
        })

        return {
            columns,
            rows
        }

        
    }


    renderOutput() {
        if(this.props.data.length === 0){
            return (
                    <div className="p-3 text-center" style={{height:'10%'}}>
                        No files to display.
                    </div>
            );
        }
        else {

            const groupedData = new Map();
            this.props.data.forEach(item => {
                console.log(item);
                const collection = groupedData.get(item.vendorName) || [];
                collection.push(item);
                groupedData.set(item.vendorName, collection);
            });

            const output =  [];

            console.log(groupedData)

            groupedData.forEach((values, key) => {
                output.push(
                    <>
                        <div className="row">
                            <div className="col">{key}</div>
                        </div>
                        <div className="row">
                            <div className="col">
                                <MDBDataTableV5 
                                    data={this.renderTableBody(values)} 
                                    searching={false} 
                                    entries={3} 
                                    entriesOptions={[3,5,10, 15]} 
                                    sortable={false} 
                                    striped
                                    responsive 
                                />
                            </div>
                        </div>
                    </>
                )
            });

            return output
        }
    }

    renderFileInfo = () => {
        if(this.state.selectedFile){
            // console.log(this.state.selectedFile.type, this.state.selectedFile.createdAt)
            return (
                <div className="container-fluid py-2">
                    <div className="row">
                        <div className="col">
                            <img src="https://img.icons8.com/dusk/64/000000/ms-excel.png"/>
                            <a className="d-none" href="https://icons8.com/icon/42965/microsoft-excel">Microsoft Excel icon by Icons8</a>
                        </div>
                        <div className="row">
                            <div className="col">
                                {this.state.selectedFile.type}
                            </div>
                        </div>
                        <div className="row">
                            <div className="col">
                                Last Modified : {this.state.selectedFile.createdAt}
                            </div>
                        </div>
                    </div>
                </div>
            )
        }
        return null;
    }

    render(){
       
        return (
            
            <div className="row justify-content-center py-4">
                <SendEmailModal show={this.state.show} handleClose={this.handleClose} filePath={this.state.selectedFile?this.state.selectedFile.filePath:null}>
                    {this.renderFileInfo()}
                </SendEmailModal>
                <div className="col-lg-8 col-md-12 col-sm-12 col-12">
                    <div className="h5 p-3 w-100 text-center text-primary">{this.props.header}</div>
                    <div className="container-fluid">
                        {this.renderOutput()}
                    </div>
                </div>
            </div>
        ) ;
    }
}

export default VendorFileList;