import React from 'react';
import { Button } from 'reactstrap';

class QPost extends React.Component {
      render() {
        return (
        <div className="q-post">

            <h3>Title: {this.props.title}</h3>
            <div className="q-post-date"><p>{this.props.date}</p></div>
            <div className="q-post-author"><p>By {this.props.author}</p></div>
            <div className="q-post-text">
                {this.props.text}
            </div>
            <Button
                                        tag="a"
                                        color="success"
                                        size="large"
                                        href="http://reactstrap.github.io"
                                        target="_blank"
                                    >
                                        Test ReactStrap
                                    </Button>
            <hr/>
        </div>
        );
      }
}
class QPostList extends React.Component{
    constructor(){
        super();
        this.state ={
            posts: [],
        }
    }
    componentDidMount(){
        fetch(window.__SVR_DATA__.api_addr + "/posts/").then(results => {
            return results.json();
        }).then(data => {
            let posts = data.results.map((data) => {
                return(
                    <QPost
                        key={data.post_id}
                        title={data.post_title}
                        date={data.post_date}
                        author={data.post_author}
                        text={data.post_text} />
                )
            })
            this.setState({posts: posts});
        })
    }
    render(){
        return <div>{this.state.posts}</div>
    }
}

class QHome extends React.Component {
      render() {
        return (
            <div className="q-home">
                <QPostList/>
            </div>
        );
      }
}

export default QHome;