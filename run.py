from server.serverfactory import ServerFactory

server = ServerFactory()
app = server.up()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
