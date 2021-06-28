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

class FileList extends React.Component{

    state = {
        show : false,
        selectedFile : null
    }

    showModal = (type, modified_at, path) => {

        this.setState({
            show:true,
            selectedFile : {
                type,
                modified_at,
                path
            }
        })
    }
    handleClose = () => {
        this.setState({
            show : false
        })
    }
   
    renderTableBody = () => {
        const datetimeConstructor = new Intl.DateTimeFormat("en",{
            day : '2-digit',
            weekday : 'short',
            month:'long',
            year : 'numeric',
            hour:'2-digit',
            minute:'2-digit',
            hour12: true
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

        const rows = this.props.data.map(({modified_at, url, type, path}) => {
            return {
                file : (
                    <>
                        <FontAwesomeIcon icon={faFileExcel} size='2x' style={{color:'gray'}}/> {'\u00A0'}{'\u00A0'} {datetimeConstructor.format(modified_at)}
                    </>
                ),
                action : (
                    <>
                        <div className="d-flex">
                            <div className="d-inline-block px-2">
                                <MDBTooltip domElement tag="span" placement="top">
                                    <a onClick={() => this.showModal(type,datetimeConstructor.format(modified_at), path)}><span className="text-primary"> <FontAwesomeIcon icon={faEnvelopeOpen} size='2x'/></span></a>
                                    <span>Send via email</span>         
                                </MDBTooltip>
                            </div>
                            <div className="d-inline-block px-2">
                                <MDBTooltip domElement tag="span" placement="top">
                                    <a href={url} target="_blank"><span className="text-primary"> <FontAwesomeIcon icon={faCloudDownloadAlt} size='2x'/></span></a>
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

        return this.props.data.map(({modified_at, url, type, path}) => {
            
            return (
                <tr>
                    
                    <td>
                        <FontAwesomeIcon icon={faFileExcel} size='2x' style={{color:'gray'}}/> {'\u00A0'}{'\u00A0'} {datetimeConstructor.format(modified_at)}
                    </td>
                    <td>
                        <div className="d-inline-block px-3">
                            <MDBTooltip domElement tag="span" placement="top">
                                <a onClick={() => this.showModal(type,datetimeConstructor.format(modified_at), path)}><span className="text-primary"> <FontAwesomeIcon icon={faEnvelopeOpen} size='2x'/></span></a>
                                <span>Send via email</span>

                               
                            </MDBTooltip>
                        </div>
                        <div className="d-inline-block px-3">
                        <MDBTooltip domElement tag="span" placement="top">
                                <a href={url} target="_blank"><span className="text-primary"> <FontAwesomeIcon icon={faCloudDownloadAlt} size='2x'/></span></a>
                                <span>Download File to this device.</span>

                            </MDBTooltip>
                        </div>
                    </td>
                </tr>
            )
        })

       
    }

    renderOutput() {
        if(this.props.data.length === 0){
            return (
                    <div className="p-3" style={{height:'10%'}}>
                        <div className="container d-flex justify-content-center" style={{paddingTop:'10%'}}>
                            <LoadingSpinner  />
                        </div>
                    </div>
            );
        }
        else {
            return (
                // <MDBTable >
                //     <MDBTableHead >
                //         <tr>
                //             <th className="h6">Last Modified</th>
                //             <th className="h6">Actions</th>
                //         </tr>
                //     </MDBTableHead>
                //     <MDBTableBody>
                //         {this.renderTableBody()}
                //     </MDBTableBody>
                // </MDBTable>
                <MDBDataTableV5 
                    data={this.renderTableBody()} 
                    searching={false} 
                    entries={3} 
                    entriesOptions={[3,5,10, 15]} 
                    sortable={false} 
                    striped
                    responsive 
                />
                
            );
        }
    }

    renderFileInfo = () => {
        if(this.state.selectedFile){
            // console.log(this.state.selectedFile.type, this.state.selectedFile.modified_at)
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
                                Last Modified : {this.state.selectedFile.modified_at}
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
                <SendEmailModal show={this.state.show} handleClose={this.handleClose} path={this.state.selectedFile?this.state.selectedFile.path:null}>
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

export default FileList;