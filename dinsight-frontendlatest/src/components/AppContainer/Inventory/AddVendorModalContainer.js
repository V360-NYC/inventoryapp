import React from 'react';
import AddVendorModal from './AddVendorModal';

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
                <button className="btn btn-primary" onClick={() => this.setState({show : true})}>Add new Vendor</button>
            </>
        )
    }
}

export default AddVendorModalContainer;