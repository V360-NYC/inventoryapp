import React from 'react';
import {connect} from 'react-redux';

import FileList from './FileList';

class DisplayInventory extends React.Component{
    
    getFiles = (data, type) => {
       return this.props[data].map(({createdAt, filePath, downloadURL}) => {
           return {
               filePath,
               downloadURL,
               createdAt,
               type 
           }
       });
   }

    render(){
        return (
            <div className="container-fluid">
               
                <div className="row">
                    <div className="col">
                        <FileList data={this.getFiles('summaryFiles', 'Summary File')} header={'Summary Report'}  />
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <FileList data={this.getFiles('masterFiles', 'Master File')} header={'Master Files'} />
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <FileList data={this.getFiles('inventoryFiles', 'Inventory File')} header={'User Inventory'} />
                    </div>
                </div>

            </div>
        );
    }
}

const mapStateToProps = ({user,inventoryFiles = [], summaryFiles = [], masterFiles = []}) => {
    if(!user)return {};

    return {
        userID : user.uid,
        inventoryFiles,
        summaryFiles,
        masterFiles
    }
}

export default connect(mapStateToProps, {})(DisplayInventory);