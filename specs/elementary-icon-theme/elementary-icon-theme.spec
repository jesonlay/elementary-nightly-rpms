%global srcname icons

Name:           elementary-icon-theme
Summary:        Icons from the Elementary Project
Version:        4.3.1+git%{date}.%{commit}
Release:        2%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake


%description
This is an icon theme designed to be smooth, sexy, clear, and efficient.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

# Clean up stuff
rm %{buildroot}/.VolumeIcon.png
rm %{buildroot}/.VolumeIcon.icns

# Create icon cache file
touch %{buildroot}/%{_datadir}/icons/elementary/icon-theme.cache


%transfiletriggerin -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :


%files
%doc AUTHORS CONTRIBUTORS README.md
%license COPYING

%{_datadir}/icons/elementary/
%ghost %{_datadir}/icons/elementary/icon-theme.cache


%changelog
* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180104.200132.842f5c35-2
- Add file triggers to replace scriptlets.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git180104.200132.842f5c35-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171217.012202.430d3efe-2
- Merge .spec file from fedora.

* Sun Dec 17 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171217.012202.430d3efe-1
- Update to latest snapshot.

* Mon Dec 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171204.174803.abee5f0d-1
- Update to latest snapshot.

* Fri Dec 01 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171130.221733.f307c80e-1
- Update to latest snapshot.

* Tue Nov 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171127.232552.330a640b-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171118.192425.17e40d31-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171117.041239.0a372227-1
- Update to latest snapshot.

* Sun Nov 05 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171105.212540.eff997c8-1
- Update to latest snapshot.

* Tue Oct 31 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171031.165154.01a6384e-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1+git171024.202106.bc9d5b1e-1
- Update to version 4.3.1.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git171024.202106.bc9d5b1e-1
- Update to latest snapshot.

* Mon Oct 23 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git171023.175241.f00a2f1d-1
- Update to latest snapshot.

* Sun Oct 22 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git171021.200313.29f12915-1
- Update to latest snapshot.

* Tue Sep 26 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170926.163628.008fb75e-1
- Update to latest snapshot.

* Sun Sep 24 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170924.142954.4bb1abfc-1
- Update to latest snapshot.

* Thu Sep 21 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170920.201212.339182ad-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170918.235930.5a2c9a69-1
- Update to latest snapshot.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170917.200704.44e643ac-1
- Update to latest snapshot.

* Wed Aug 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170829.210813.59c65c10-1
- Update to latest snapshot.

* Mon Aug 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170828.172704.13f083de-1
- Update to latest snapshot.

* Wed Aug 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170801.230140.4db8a471-1
- Update to latest snapshot.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170801.180037.ab2f6dd4-1
- Update to latest snapshot.

* Wed Jul 26 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170726.043211.a99da6e8-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170725.165823.846f65b9-1
- Update to latest snapshot.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170725.000617.73a04048-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170724.171630.0159920a-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170723.180712.42616d9d-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170720.175004.9bc143c7-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170719.224345.b77e4bbb-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0+git170719.165009.88ab6509-1
- Update to version 4.2.0.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170719.165009.88ab6509-1
- Update to latest snapshot.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170719.005923.c09f5307-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170711.191425.dc5703a1-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170630.014303.36f3efa5-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170628.033332.28ab75a3-1
- Update to latest snapshot.

* Sun Jun 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170624.205141.f074ae50-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170618.021742.1b82f02e-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170617.032943.cec13040-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170616.185512.7bce970d-1
- Update to latest snapshot.

* Fri Jun 16 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170616.032948.3433c01d-1
- Update to latest snapshot.

* Thu Jun 15 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170615.182938.4680e317-1
- Update to latest snapshot.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170614.201622.fffd5678-1
- Update to latest snapshot.

* Mon Jun 12 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170612.155214.ede84605-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170603.164225.de764cb8-1
- Update to latest snapshot.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170530.161436.39bb46c5-1
- Update to latest snapshot.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0+git170515.032734.b9521515-1
- Update to version 4.1.0.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170515.032734.b9521515-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170510.120627.b10695b2-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170509.114442.2b4de6ea-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170507.114259.bd97bca8-1
- Update to latest snapshot.

* Fri May 05 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170504.225855.1f24c818-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170504.121945.37f345e3-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170503.155115.b3aa4e2c-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170503.115336.5a241a59-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170502.134849.6e3679ff-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170501.172536.2b901ccd-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170425.165220.c27c0112-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170320.103314.77291de6-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170227.130409.6c5effa8-1
- Update to version 4.0.3.

* Sat Mar 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170227.130409.6c5effa8-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170202.220804.fdbcf47b-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170116.125315.83c6f271-2
- Sync spec with fedora package.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170116.125315.83c6f271-1
- Update to version 4.0.2.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git170116.125315.83c6f271-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161221.100345.7e9575f6-1
- Update to version 4.0.1.1.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161221.100345.7e9575f6-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161218.084045.bacf93dc-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161216.191803.a6743da8-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161215.100355.c2e60822-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161214.122150.7d0c52c6-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161201.145742.c646545c-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161130.143018.f751b03b-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161025.124600.181998c1-1
- Update to version 4.0.1.1.

* Tue Oct 25 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161025.124600.181998c1-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161018.124244.8e52e9b7-1
- Update to latest snapshot.

* Wed Oct 12 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161011.215041.c95cfe62-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161011.103850.0e1a7d60-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git160920.130844.24a317fc-1
- Update to version 4.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160920.130844~24a317fc-2
- Spec file cleanups.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160920.130844~24a317fc-1
- Update to latest snapshot.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160919.212218~47f10bd5-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160911.193229~1d70ea96-1
- Update to version 4.0.1.


