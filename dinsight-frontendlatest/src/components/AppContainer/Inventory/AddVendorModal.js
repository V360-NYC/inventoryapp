import React from 'react';
import { Modal } from 'react-bootstrap';
import { Formik, Form, Field } from 'formik'



class AddVendorModal extends React.Component{
    initialValues = {
        VENDORNAME : ''
    }

    render(){
        const { handleClose, handleSubmit, show} = this.props;
        return (
            <Modal show={show} onHide={handleClose}>
                <Formik
                    initialValues={this.initialValues}
                    onSubmit={(data) => {
                        handleClose();
                        handleSubmit(data);
                    }}
                >
                
                    <Form>
                        <Modal.Body>
                            <div className="container">
                                <div className="row">
                                    <div className="col p-2 text-center">
                                        <div className="h3">Add Vendor</div>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col text-center">
                                        <label htmlFor="vendor-name">Vendor Name</label>
                                        <Field 
                                            name="VENDORNAME"
                                            className="form-control"
                                            type="text"
                                        />
                                        
                                    </div>
                                </div>
                            </div>
                        </Modal.Body>
                        <Modal.Footer>
                            <button className="btn btn-primary " type="submit">Add</button>
                            <button className="btn btn-danger float-end" type="button" onClick={handleClose}>cancel</button>
                        </Modal.Footer>
                    </Form>                
                </Formik>
            </Modal>
        )
    }
}

export default AddVendorModal;