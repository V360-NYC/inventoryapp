
import React from 'react';
import { MDBDataTable, MDBDataTableV5, MDBTable, MDBTableHead, MDBTableBody } from 'mdbreact';

class DataTable extends React.Component{
    render(){
        return (
            
                // <MDBTable responsive bordered striped>
                //     <MDBTableHead columns={this.props.data.columns} />
                //     <MDBTableBody rows={this.props.data.rows} />
                // </MDBTable>
            
                <MDBDataTableV5 
                    small
                    searchTop
                    responsive
                    searchBottom={false}
                    data={this.props.data} 
                />
        );
    }
}

export default DataTable;