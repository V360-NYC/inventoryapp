import React from 'react';
import {connect} from 'react-redux';

import {listBucketObjects} from '../../util/firebase-storage';
import {getFiles} from '../../util/firebase-realtime';

import FileList from './FileList';

class DisplayInventory extends React.Component{
    state = {
        inventoryFiles : [],
        masterFiles : [],
        summaryFiles : []
    }

    fetchBucketFiles = async (folders, type) => {
        var data = [];
            
        for (let i = 0; i < folders.prefixes.length; i++) {
            const folderRef = folders.prefixes[i];
            
            const files = await folderRef.listAll();
            
            for (let j = 0; j < files.items.length; j++) {
                const fileRef = files.items[j];
                
                const downloadURL = await fileRef.getDownloadURL();
                const meta = await fileRef.getMetadata();
                
                data.push({
                    modified_at : new Date(meta.updated),
                    url : downloadURL,
                    path : `${meta.bucket}/${meta.fullPath}`,
                    type
                })
                
            }
        }
        
        data.sort((item1, item2) => {
            return item2.modified_at - item1.modified_at
        })
        
        return data;
       
    }

    // fetchSummaryAndMasterFiles = async (files, type) => {
    //     const data = [];

    //     for (let j = 0; j < files.items.length; j++) {
    //         const fileRef = files.items[j];

    //         const downloadURL = await fileRef.getDownloadURL();
    //         const meta = await fileRef.getMetadata();
            
    //         data.push({
    //             url : downloadURL,
    //             modified_at : new Date(meta.updated),
    //             path : `${meta.bucket}/${meta.fullPath}`,
    //             type
    //         })
            
    //     }
    //     data.sort((item1, item2) => {
    //         return item2.modified_at - item1.modified_at
    //     })

    //     return data;
    // }

    
    componentDidMount = () => {

        // getFiles(`linkPointers/${this.props.userID}`);

        listBucketObjects(`dinsight-user-inventory-test/${this.props.userID}`)
        .then(async (response) => {
            const inventoryFiles = await this.fetchBucketFiles(response, 'Inventory File')
            this.setState({inventoryFiles})
        })
        .catch(err => console.error(err));

        listBucketObjects(`dinsight-master-files-test/${this.props.userID}`)
        .then(async (response) => {
            const masterFiles = await this.fetchBucketFiles(response, 'Master File')
            this.setState({masterFiles})
        })
        .catch(err => console.error(err));

        listBucketObjects(`dinsight-summary-files-test/${this.props.userID}`)
        .then(async (response) => {
            const summaryFiles = await this.fetchBucketFiles(response, 'Summary File')
            this.setState({summaryFiles})
        })
        .catch(err => console.error(err));
        
    }

   

    render(){
        return (
            <div className="container-fluid">
               
                <div className="row">
                    <div className="col">
                        <FileList data={this.state.summaryFiles} header={'Summary Report'} showModal={this.showModal} />
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <FileList data={this.state.masterFiles} header={'Master Files'} showModal={this.showModal}/>
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <FileList data={this.state.inventoryFiles} header={'User Inventory'} showModal={this.showModal}/>
                    </div>
                </div>

            </div>
        );
    }
}

const mapStateToProps = (state) => {
    if(!state.user)return {};

    return {
        userID : state.user.uid
    }
}

export default connect(mapStateToProps, {})(DisplayInventory);