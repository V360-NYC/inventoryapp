import React from 'react';
import { postQuery } from '../util/firebase-firestore'


import {connect} from 'react-redux';

class QuickSearch extends React.Component{

    handleQuerySelect = (event) => {
        const {uid, displayName, photoURL} = this.props.user;
        console.log(event.target.getAttribute('value'));
        postQuery(`chats/${uid}/messages`,{
            botReply:false,
            name: displayName,
			text: event.target.getAttribute('value'),
			photoUrl: photoURL,
			uid: uid,
			timeStamp: new Date().valueOf(),
			device: "desktop"
        })
     
    }

    renderQuickSearcTable = (colors, clarity, stats, colorValues, clarityValues, caratValues) => {
        const rows = []

        for(let i = 0;i < colors.length;i++){
            for(let j = 0;j < clarity.length;j++){
                const row = [<td>{clarity[j]}</td>];
                for(let k = 0;k < stats[i][j].length;k++){
                    if(stats[i][j][k][0] === 0){
                        row.push(
                            <td className="text-primary">
                                None
                            </td>
                        )
                    }
                    else{
                        row.push(
                            <td>
                                <a href="#"
                                    className="text-primary"
                                    value={`${colorValues[i]} ${clarityValues[j]} ${caratValues[k]} ${stats[i][j][k][1]} ${stats[i][j][k][2]}`}
                                    onClick={this.handleQuerySelect}
                                >
                                {stats[i][j][k][0]} ( ${stats[i][j][k][1]} - ${stats[i][j][k][2]})
                                </a>
                            </td>
                        )
                    }
                }
                rows.push(row);
            }
        }

        return rows.map((row, index) => {
            if(index%5 === 0){
                return (
                    <tr>
                        <td rowSpan="5">{colors[index%5]}</td>
                        {row}
                    </tr>
                )
            }

            return <tr>{row}</tr>
        })


    }
    render(){
        const {colors, clarity, stats, colorValues, clarityValues, caratValues} = this.props;
        // console.log(colors, clarity, stats, colorValues, clarityValues, caratValues)
        return (
            <div className="table-responsive">
                <table className="table table-bordered align-middle text-center table-sm">
                    <thead>
                        <tr>
                            <th  rowSpan="2" >Color</th>
                            <th  rowSpan="2">Clarity</th>
                            <th colSpan="4" >Carat</th>
                        </tr>
                        <tr>
                            
                            <th>0.18 to 0.45</th>
                            <th>0.46 to 0.95</th>
                            <th>0.96 to 1.45</th>
                            <th>1.46 to 10.0</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderQuickSearcTable(colors, clarity, stats, colorValues, clarityValues, caratValues)}
                    </tbody>
                </table>
            </div>
        )
    }
}


const mapStateToProps = (state) => {
    if(!state.user)return;

    return {
        user : state.user
    }
}
export default connect(mapStateToProps,{})(QuickSearch);