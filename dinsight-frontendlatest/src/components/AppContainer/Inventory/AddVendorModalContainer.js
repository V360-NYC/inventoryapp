import React from 'react';
import AddVendorModal from './AddVendorModal';
import '../../../assets/css/Messenger.css'
import {postQuery} from '../../util/firebase-firestore';

class AddVendorModalContainer extends React.Component{
    state = {
        show : false
    }

    handleClose = () => {
        this.setState({
            show : false
        })
    }

    handleSubmit = (data) => {
        // upload vendor info to firestore
        console.log(data);
        this.props.addNewVendor(data);        
    }

    render(){
        return (
            <>
                <AddVendorModal 
                    handleClose={this.handleClose}
                    handleSubmit={this.handleSubmit}
                    show={this.state.show}
                />
                <button style={{backgroundColor:'#4285f4'}} className="btn button-style" onClick={() => this.setState({show : true})}>Add new Vendor</button>
            </>
        )
    }
}

export default AddVendorModalContainer;