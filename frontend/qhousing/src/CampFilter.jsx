import React from 'react';

export default class CampFilter extends React.Component {

  render() {
      console.log(this.props.inuse)
    return (
      <div className="col-sm-2">
          <label ref="text">{this.props.id}</label>
          <select
              className="selectbox"
              value={this.props.inuse}
              id={this.props.id}
              defaultChecked={this.props.inuse}
              onChange={(e) => this.props.changeFilter(this.props.id, e.target.value)}>
              {this.props.options.map(option => {
                return <option value={option} key={option} >{option}</option>
        })}
          </select>
       </div>
      )
  }
}
