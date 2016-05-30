Summary:        Audience video player
Name:           audience
Version:        0.1.0.2~rev%{rev}
Release:        3%{?dist}
License:        GPLv3
URL:            http://launchpad.net/audience

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)


%description
A modern video player that brings the lessons learned from the web home to the desktop.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang audience


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/audience.desktop

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml
# Validation of files failed


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files       -f audience.lang
%doc AUTHORS README
%license COPYING

%{_bindir}/audience

%{_datadir}/appdata/audience.appdata.xml
%{_datadir}/applications/audience.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.audience.gschema.xml


%changelog
* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev584-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev584-2
- Update for packaging changes.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev584-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev583-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev582-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev581-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev581-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev580-2
- Update for packaging changes.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev580-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev579-1
- Update to new upstream snapshot.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev578-2
- Add BR: clutter-gst-3.0.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev578-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev576-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev575-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev574-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev573-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev571-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev570-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev569-1
- Update to new upstream snapshot.

* Sat Jan 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev568-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev567-1
- Update to new upstream snapshot.

* Fri Dec 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev566-1
- Update to new upstream snapshot.

* Thu Dec 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev565-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev564-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev563-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev562-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev561-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev560-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev559-2
- Modernise spec. Fix build by including new appdata file. Validate desktop and
  appdata file.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev559-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev556-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev554-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev553-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev552-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev551-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev550-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev549-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev548-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev547-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev546-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev545-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev544-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev543-1
- Update to new upstream snapshot.

* Thu Oct 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev541-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev540-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev539-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev538-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev537-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev536-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev535-2
- rebuild trigger for granite soname bump

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev535-1
- Update to new upstream snapshot.

* Sun Aug 16 2015 Fabio Valentini - 0.1.0.2~rev534-1
- Bump to correct upstream version (0.1.0.2).

* Sun Aug 16 2015 Fabio Valentini - 0.1.0.1~rev534-1
- Update to upstream bzr snapshot revno 534.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev531-1
- Update to bzr snapshot revno 531.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev529-2
- Use %doc and %license macros.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev529-1
- Update to bzr snapshot revno 529.
- Use more spec macros.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev498-5
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev485-4
- Update to latest bzr snapshot.

* Sun Jan 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev482-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev481-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev479-1
- Update to bzr revision 479.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev477-1
- Initial package.
