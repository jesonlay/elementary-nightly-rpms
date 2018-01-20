%global srcname stylesheet

Name:           elementary-theme
Summary:        elementary GTK+ Stylesheet
Version:        5.1.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.


%package        gtk2
Summary:        elementary GTK+ Stylesheet for GTK+2

Requires:       %{name} = %{version}-%{release}
Requires:       gtk-murrine-engine

Supplements:    (%{name} and gtk2)

%description    gtk2
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+2 theme.


%package        gtk3
Summary:        elementary GTK+ Stylesheet for GTK+3

Requires:       %{name} = %{version}-%{release}

Supplements:    (%{name} and gtk3)

%description    gtk3
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+3 theme.


%package        plank
Summary:        elementary GTK+ Stylesheet for plank

Requires:       %{name} = %{version}-%{release}

Supplements:    (%{name} and plank)

%description    plank
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the plank theme.


%prep
%autosetup


%build
# Nothing to do


%install
mkdir -p %{buildroot}/%{_datadir}/themes/elementary

cp -p index.theme %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.22 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr plank %{buildroot}/%{_datadir}/themes/elementary/


%files
%doc AUTHORS CONTRIBUTORS README.md
%license COPYING

%dir %{_datadir}/themes/elementary
%{_datadir}/themes/elementary/index.theme

%files          gtk2
%{_datadir}/themes/elementary/gtk-2.0/

%files          gtk3
%{_datadir}/themes/elementary/gtk-3.0/
%{_datadir}/themes/elementary/gtk-3.22/

%files          plank
%{_datadir}/themes/elementary/plank/


%changelog
* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180120.212024.8468054a-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180118.181744.f0dd2c40-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git180109.204946.0347dcdc-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171231.175903.886c9630-2
- Merge .spec file from fedora.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171231.175903.886c9630-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171229.222307.18ec68f6-1
- Update to latest snapshot.

* Thu Dec 28 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171228.183102.137afe69-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171212.203746.d4766477-1
- Update to latest snapshot.

* Mon Dec 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171211.183836.18d919e6-1
- Update to latest snapshot.

* Wed Nov 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171129.182341.bd7fc6bc-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171116.234955.383aa236-1
- Update to latest snapshot.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171114.224021.2b2e0523-1
- Update to latest snapshot.

* Sun Oct 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171029.214602.e3d44a58-1
- Update to latest snapshot.

* Sat Oct 28 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171028.003928.be507119-1
- Update to latest snapshot.

* Wed Oct 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171017.211349.a244d049-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git171012.163047.a6e541d3-1
- Update to latest snapshot.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.1+git170925.140355.6a96d0f3-1
- Update to version 5.1.1.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170925.140355.6a96d0f3-1
- Update to latest snapshot.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170917.191146.384412d6-1
- Update to latest snapshot.

* Thu Aug 31 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170831.163958.d4137cb0-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170830.192346.73e8e2cb-1
- Update to latest snapshot.

* Sat Aug 26 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170826.203852.27c0fe5f-1
- Update to latest snapshot.

* Sat Aug 26 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170826.195943.65c8b062-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170819.171047.2f485fb1-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170819.165546.77d918ca-1
- Update to latest snapshot.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 5.1.0+git170810.193052.29777e21-1
- Update to version 5.1.0.

* Thu Aug 10 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170810.193052.29777e21-1
- Update to latest snapshot.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170808.152138.cde785f6-1
- Update to latest snapshot.

* Sat Jul 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170729.203948.5a0b0bbc-1
- Update to latest snapshot.

* Thu Jul 27 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170727.011959.ae7b021a-1
- Update to latest snapshot.

* Wed Jul 26 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170726.141331.49869a84-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170725.033915.06327c6d-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170722.201500.a27fee78-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170719.161159.a057c8af-1
- Update to latest snapshot.

* Tue Jul 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170718.170824.1e91f11f-1
- Update to latest snapshot.

* Mon Jul 17 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170717.144046.d771a6dc-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170716.193802.ffa88847-1
- Update to latest snapshot.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170715.183054.2e1b2771-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170714.174844.9b9cf189-1
- Update to latest snapshot.

* Fri Jul 14 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170714.132038.f68e4d02-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170711.172317.224c8b63-1
- Update to latest snapshot.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170710.191636.0676d4d9-2
- Add GTK 3.22 theme to gtk3 subpackage.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170710.191636.0676d4d9-1
- Update to latest snapshot.

* Mon Jul 10 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170710.063940.73154fb8-1
- Update to latest snapshot.

* Sun Jul 09 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170709.163839.1f26c7c2-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170707.193146.fcadef2d-1
- Update to latest snapshot.

* Fri Jul 07 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170707.025047.0102c0fe-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170617.153121.5696951d-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170607.205340.72f9a91e-1
- Update to latest snapshot.

* Wed May 24 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170524.154507.546aeb0e-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170506.180348.62761903-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170501.094928.bf0893a0-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170430.094741.471ffaeb-2
- Adapt to upstream file changes.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170430.094741.471ffaeb-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170212.162057.5f600c6b-1
- Update to version 5.0.4.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170128.184610.01d0411e-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170128.184610.01d0411e-2
- Sync spec with fedora package.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170115.161326.548fac7c-1
- Update to version 5.0.3.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git170115.161326.548fac7c-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161218.174932.727c158a-1
- Update to version 5.0.2.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161218.174932.727c158a-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161015.175037.cb6b93eb-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160927.144324.36a46bf9-2
- Spec file cleanups.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160927.144324.36a46bf9-1
- Update to latest snapshot.

* Sun Sep 25 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160925.113001.778259b4-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160923.173728.192e7cc8-1
- Update to version 5.0.2.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git160923.173728.192e7cc8-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git160922.142219.f2f734b3-1
- Update to version 5.0.1.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160919.163423~877fab28-1
- Update to latest snapshot.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160919.134452~ad45ee14-1
- Update to latest snapshot.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160916.205458~8189f96b-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160911.211643~3457221a-1
- Update to version 5.0.1.


