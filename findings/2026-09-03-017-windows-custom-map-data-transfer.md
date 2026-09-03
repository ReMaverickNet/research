# FINDING-2026-09-03-017: Creative sessions request server-delivered custom-map data

Status: observed
Confidence: high
First observed: 2026-08-30
Sessions: Windows Tye logs

## Observation

`LogCC1047CustomMapSupport` records seven completed server-delivered map-data transfers across the supplied August 30–September 2 logs. All seven are associated with `/MAP_Creative_WetOcean/WetOcean_Main` except the initial September 2 `Creative_EmptySpace` session, which is associated with `/MAP_Creative_EmptySpace/EmptySpace_Main` in the preceding welcome event.

Observed compressed/uncompressed pairs are:

- `295084` → `4863514` bytes (twice)
- `322454` → `4298790` bytes (three times)
- `330169` → `5036717` bytes (once)
- `301203` → `4010411` bytes (once)

Every transfer arrives as repeated chunks, is completed successfully, and is followed by custom-map initialisation. Two of the seven transfers fall inside the supplied September 2 filtered PCAP window (04:56:55 and 05:53:43); the 07:18:56 transfer is outside that PCAP.

## Evidence

- `logs/game/2026-09-03-001-tye-session-excerpts.txt`
- `archive/2026-09-03-001/custom-map-transfers.csv`
- `archive/2026-09-03-001/event-index.csv`

## Interpretation

Creative functionality can depend on data delivered by the authoritative server rather than being entirely local. Repeated identical compressed sizes across separate WetOcean sessions show that the same-size map-data payload is reused, although the logs do not provide a content hash or prove that equal sizes mean identical bytes.

## Alternatives / limitations

The logs do not expose the transport framing, chunk protocol or whether the data is carried inside ordinary Unreal replication/RPC machinery. Because the matching filtered PCAP omits the authoritative endpoint, this contribution does not yet bind the map-data chunks to packet-level transport.

## Next test

Repeat a Creative/WetOcean session with the raw wide PCAP preserved, then align every `Received map data chunk` timestamp with packet directions and lengths. Repeat with the same map cached locally.

## AI analysis

AI grouped transfer records and calculated repeated size pairs/durations from the supplied logs. The event count and byte totals were checked directly against the raw log text.
