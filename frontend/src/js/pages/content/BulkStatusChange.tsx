import React, { useState, useEffect } from "react"
import {Button, Typography} from "@material-ui/core"
import { GenericDialog} from "solarspell-react-lib"
import {useCCDispatch, useCCSelector} from "../../hooks"
import {useImmer} from "use-immer"
import {bulk_status_change} from "../../state/content"
export default () => {
    const [open, setOpen] = useState(false)
    const content_selected = useCCSelector(state => state.content.selected);
    const dispatch = useCCDispatch()
    return <>
    <Button onClick={_ => setOpen(true)}>Bulk Status Edit</Button>
    <GenericDialog 
            open={open}
            title={`Bulk Edit ${content_selected.length} Items`}
            onClose={_ => setOpen(false)}
            actions={<>
                <Button color="secondary" onClick={() => setOpen(false)}>Cancel</Button>
                <Button
                    onClick={() => {
                        setOpen(false)
                        dispatch(bulk_status_change({
                            // to_edit: Object.values(to_edit).reduce((acc, current) =>
                            //     acc.concat(current), []
                            to_edit:[],  }))
                    }}
                >
                     Edit Status
                    </Button>
            </>}
        >
    <Typography style={{minWidth: "400px"}}>Edit Content Status</Typography>
// How to do Drop down

    </GenericDialog>
    </>

} 
