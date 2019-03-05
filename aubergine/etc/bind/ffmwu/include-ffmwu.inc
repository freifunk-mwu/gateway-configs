; BIND data file for zone ffmwu.org.
;
$TTL    600
@       IN      SOA     aubergine.ffmwu.org. hostmaster.ffmwu.org. (
                     2019030500         ; Serial
                             2h         ; Refresh
                             1h         ; Retry
                            41d         ; Expire
                            300 )       ; Negative Cache TTL

; internal ns server
@                       IN      NS      wasserfloh.ffmwu.org.
@                       IN      NS      spinat.ffmwu.org.
@                       IN      NS      lotuswurzel.ffmwu.org.
@                       IN      NS      ingwer.ffmwu.org.
@                       IN      NS      uffschnitt.ffmwu.org.
