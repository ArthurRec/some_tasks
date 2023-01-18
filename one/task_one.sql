select sum(viewers) / 60 as hours_watched, gm.publisher
from streamers as st
join games_metadata as gm
on st.game = gm.game
where st.timestamp >= extract(epoch from timestamp '2020-04-01 00:00:00')
    and st.timestamp < extract(epoch from timestamp '2020-07-01 00:00:00')
group by gm.publisher
order by hours_watched desc
limit 10;