import impala.dbapi
import happybase

connect = happybase.Connection(host='hadoop3', port=9090, timeout=None, autoconnect=True,
                     table_prefix=None, table_prefix_separator=b'_', transport='buffered', protocol='binary')
connect.open()

families = {
    "cf":dict(),
    "df":dict()
}

connect.create_table('jobdata',families)

connect.close()