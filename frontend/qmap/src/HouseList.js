import React, {Component} from 'react'

class HouseList extends Component {
    render() {
        return (
            <div className="IamHouse">
                {this.props.name}
            </div>
        )
    }
}

export default HouseList