# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI, GET, POST

class Volume(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.subid = None
        self.date_created = None
        self.cost_per_month = None
        self.status = None
        self.size_gb = None
        self.dcid = None
        self.attached_to_subid = None
        self.label = None

        super(Volume, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, volume_id):
        """
        Class method that will return an Volume object by ID.
        """
        volume = cls(token=api_token, subid=volume_id)
        volume.load()
        return volume

    def load(self):
        """
        Documentation: https://www.vultr.com/api/#block_block_list
        """
        volumes = self.get_data("block/list")

        for volume in volumes:
            if volume["SUBID"] == self.subid:
                for attr in volume.keys():
                    setattr(self, attr.lower(), volume[attr])

        return self

    def create(self, *args, **kwargs):
        """
        Creates a Block Storage Volume.

        Args:
            dcid: integer - DCID of the location to create this subscription in.
            size_gb: integer - Size in GB of this subscription.

        Optional Args:
            label: string - Text Label that will be associated with this subscription.
        """
        input_params = {
            'DCID': self.dcid,
            'size_gb': self.size_gb,
            'label': self.label
        }

        data = self.get_data(
            "block/create",
            type=POST,
            params=input_params
        )

        if data:
            self.subid = data['SUBID']

        return self

    def delete(self, *args, **kwargs):
        """
        Deletes a Block Storage Volume.

        Args:
            subid: integer - Subscription id of the volume.
        """
        input_params = {
            'SUBID': self.subid
        }

        data = self.get_data(
            "block/delete",
            type=POST,
            params=input_params
        )

        return self

    def attach(self, *args, **kwargs):
        """
        Attaches a Block Storage Volume with an Instance.

        Args:
            subid: integer - Subscription id of the volume to attach.
            attached_to_subid: integer - Subscription id of the instance to attach to.
        """
        input_params = {
            'SUBID': self.subid,
            'attach_to_SUBID': self.attached_to_subid
        }

        data = self.get_data(
            "block/attach",
            type=POST,
            params=input_params
        )

        return self

    def detach(self, *args, **kwargs):
        """
        Detaches a Block Storage Volume from an Instance.

        Args:
            subid: integer - Subscription if of the volume to detach.
        """
        input_params = {
            'SUBID': self.subid
        }

        data = self.get_data(
            "block/detach",
            type=POST,
            params=input_params
        )

        return self

    def __str__(self):
        return "<Volume: %s %s %s>" % (self.subid, self.label, self.size_gb)
