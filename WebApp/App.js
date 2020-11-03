import * as React from 'react';
import { WebView } from 'react-native-webview';

export default class App extends React.Component {
  render() {
    return <WebView source={{ uri: 'https://animalface.wookingwoo.com' }} style={{ marginTop: 20 }} />;
  }
}


// test